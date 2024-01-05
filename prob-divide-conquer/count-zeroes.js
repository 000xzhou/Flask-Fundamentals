function countZeroes(listItem) {
  /**
   * Given an array of 1s and 0s which has all 1s first followed by all 0s,
   * write a function called countZeroes,
   * which returns the number of zeroes in the array.
   */

  if (listItem[listItem.length - 1] === 1) {
    return 0;
  }

  let left = 0;
  let right = listItem.length - 1;
  while (left < right) {
    let mid = Math.floor((left + right) / 2);

    if (listItem[mid] === 1) {
      // look for right path
      left = mid + 1;
    } else {
      //look for left path
      right = mid;
    }
  }

  // Number of zeroes is the length of the array minus the index of the first zero
  return listItem.length - left;
}

module.exports = countZeroes;
