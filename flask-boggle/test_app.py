from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

class FlaskTests(TestCase):
    def test_get_index(self):
        """Test if index html is display """
        
        with app.test_client() as client:
            """Test if the game load"""
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form action="/" method="post" id="guess">', html)
            self.assertIn('game', session)
            self.assertIsNone(session.get('game_stats'))
                        
    def test_session_game_stats(self):
        """Test if the game stats load"""
        with app.test_client() as client:
            res = client.get('/start')
            self.assertEqual(res.status_code, 200)
            self.assertEqual(session["game_stats"], {"best_score":0, "total_games":0})
    
    def test_session_game_stats_v2(self):
        """Test if the game stats update"""
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session["game_stats"] = {"best_score":1, "total_games":2}
            res = client.post('/score', json={"score": 2})
            self.assertEqual(res.status_code, 200)
            with client.session_transaction() as session:
                self.assertEqual(session["game_stats"], {"best_score": 2, "total_games": 3})
            
    def test_valid_word(self):
        """Test if the word is in vaild and on board"""
        with app.test_client() as client:
            with client.session_transaction() as board:
                board['game'] = [["A", "a", "a", "a", "a"], 
                                  ["a", "a", "a", "a", "a"], 
                                  ["a", "a", "a", "a", "a"], 
                                  ["a", "a", "a", "a", "a"], 
                                  ["a", "a", "a", "a", "a"]]
            res = client.post('/', json={'guessWord': 'a'})
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json['result'], 'ok')
        
    def test_invalid_word(self):
        """Test if word is in the dictionary but not on board"""
        with app.test_client() as client:
            with client.session_transaction() as board:
                board['game'] = [["A", "a", "a", "a", "a"], 
                                  ["a", "a", "a", "a", "a"], 
                                  ["a", "a", "a", "a", "a"], 
                                  ["a", "a", "a", "a", "a"], 
                                  ["a", "a", "a", "a", "a"]]
            res = client.post('/', json={'guessWord': 'b'})
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json['result'], 'not-on-board')
    
    def non_english_word(self):
        """Test if word is on the board"""
        with app.test_client() as client:
            with client.session_transaction() as board:
                board['game'] = [["A", "a", "a", "a", "a"], 
                                  ["a", "a", "a", "a", "a"], 
                                  ["a", "a", "a", "a", "a"], 
                                  ["a", "a", "a", "a", "a"], 
                                  ["a", "a", "a", "a", "a"]]
            res = client.post('/', json={'guessWord': 'asfedsg'})
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json['result'], 'not-word')