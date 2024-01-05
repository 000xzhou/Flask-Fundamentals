function findRotatedIndex(arr, target) {
  /**
   * Write a function called findRotatedIndex which accepts a rotated array of sorted numbers and an integer.
   * The function should return the index of num in the array. If the value is not found, return -1.
   */
  let left = 0;
  let right = arr.length - 1;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    console.log(
      "left",
      arr[left],
      "mid",
      arr[mid],
      "right",
      arr[right],
      "target",
      target
    );

    if (arr[mid] === target) {
      return mid;
    }
    if (arr[left] <= arr[mid]) {
      if (target >= arr[left] && target < arr[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    } else {
      if (target > arr[mid] && target <= arr[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }

  return -1;
}

module.exports = findRotatedIndex;
