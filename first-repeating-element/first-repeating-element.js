Find the first repeating element in an array of integers


Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of first occurrence is smallest.

arr1 = [1,2,1,2,3,3];
arr2 = [2,1,3,5,3,2];
arr3 = [1,2,3,4,5,6];
arr4 = [10, 5, 3, 4, 3, 5, 6];

function checkDuplicate (array) {
  let tmp = [];
  for (i = 0; i < array.length; i++) {
    if (tmp.includes(array[i])) {
      return array[i];
    } else {
      tmp.push(i);
    }
  }
  
  return -1;
}

console.log(checkDuplicate(arr1));