function findFloor(listItem, target) {
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
