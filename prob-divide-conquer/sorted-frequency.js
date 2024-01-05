function findFirst(arr, target) {
  // search the left half
  let left = 0;
  let right = arr.length - 1;
  let idx = -1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (arr[mid] === target) {
      idx = mid;
      right = mid - 1;
    } else if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return idx;
}

function findLast(arr, target) {
  // search the right half
  let left = 0;
  let right = arr.length - 1;
  let idx = -1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (arr[mid] === target) {
      idx = mid;
      left = mid + 1;
    } else if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return idx;
}

function sortedFrequency(arr, target) {
  /**
   * Given a sorted array and a number,
   * write a function called sortedFrequency that counts the occurrences of the number in the array
   */
  const firstIdx = findFirst(arr, target);
  if (firstIdx === -1) return -1; // Target not found

  const lastIdx = findLast(arr, target);
  return lastIdx - firstIdx + 1;
}

module.exports = sortedFrequency;
