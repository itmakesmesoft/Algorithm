function solution(targets) {
  targets.sort((a, b) => {
    if (a[0] === b[0]) return a[1] - b[1];
    else return a[0] - b[0];
  });
  count = 0;
  let start = 0,
    end = 0;
  for (let i = 0; i < targets.length; i++) {
    const t_start = targets[i][0];
    const t_end = targets[i][1];
    if (end <= t_start) {
      start = t_start;
      end = t_end;
      count += 1;
    } else if (start < t_start && end > t_end) {
      start = t_start;
      end = t_end;
    } else if (t_end <= end) {
      end = t_end;
    } else {
      start = t_start;
    }
  }
  // console.log(count)
  return count;
}
