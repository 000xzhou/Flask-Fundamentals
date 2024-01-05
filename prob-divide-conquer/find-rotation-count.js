function findRotationCount(arr) {
  /**
   * Write a function called findRotationCount which accepts an array of distinct numbers sorted in increasing order.
   * The array has been rotated counter-clockwise n number of times. Given such an array, find the value of n.
   */
  let left = 0;
  let right = arr.length - 1;

  if (arr[left] < arr[right]) {
    return 0;
  }

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    if (arr[mid] > arr[mid + 1]) {
      return mid + 1;
    } else if (arr[left] <= arr[mid]) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return 0;
}

module.exports = findRotationCount;
