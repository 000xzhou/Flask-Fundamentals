function findFloor(listItem, target) {
  /**
   * Write a function called findFloor which accepts a sorted array and a value x,
   * and returns the floor of x in the array.
   * The floor of x in an array is the largest element in the array which is smaller than or equal to x.
   * If the floor does not exist, return -1.
   */
  let left = 0;
  let right = listItem.length - 1;
  let result = -1;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (listItem[mid] === target) {
      return listItem[mid];
    } else if (listItem[mid] < target) {
      result = listItem[mid];
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return result;
}

module.exports = findFloor;
