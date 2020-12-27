const a1 = [ -1, 0, 0, 1];
const a2 = [0, -1, 1, 0];
function getAllNeighbours(rowLen, colLen, i, j, grid, visited) {
  const res = [];
  a1.map((el, k) => {
    const newI = i + a1[k];
    const newJ = j + a2[k];
    if (newI >= 0 && newI < rowLen && newJ >= 0 && newJ < colLen && !(visited[newI][newJ]) && grid[newI][newJ] === '1') {
      res.push([newI, newJ]);
    }
  });
  return res;
}

function getDefaultArr(rows, cols) {
  const arr = [];
  for(let i = 0; i < rows; i += 1 ) {
    if(arr[i] == null) {
      arr.push([])
    };
    for (let j = 0; j < cols; j += 1) {
      arr[i].push(false)
    }
  }
  return arr;
}
function dfs(idx, grid, visited, rowLen, colLen) {
  let stack = [idx];
  while (stack.length > 0) {
    const idx = stack.pop();
    const i = idx[0];
    const j = idx[1];
    visited[i][j] = true;
    const neighbours = getAllNeighbours(rowLen, colLen, i, j, grid, visited);
    stack = stack.concat(neighbours);
  }
}
function numIslands(grid) {
  const rowLen = grid.length;
  if (rowLen === 0) {
    return 0;
  }
  const colLen = grid[0].length;
  const visited = getDefaultArr(rowLen, colLen);
  let count = 0;
  for(let i = 0; i < rowLen; i += 1) {
    for(let j = 0; j < colLen; j += 1) {
      if (!(visited[i][j]) && grid[i][j] === '1') {
        count = count + 1;
        dfs([i, j], grid, visited, rowLen, colLen);
      }
    }
  }  
  return count;
}

const testArr = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

console.log(numIslands(testArr));