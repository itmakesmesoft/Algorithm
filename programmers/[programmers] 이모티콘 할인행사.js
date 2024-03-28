function solution(users, emoticons) {
  let amounts = new Array(users.length).fill(0);
  let max_members = 0,
    max_amounts = 0;
  const dfs = (emoticonIndex) => {
    if (emoticonIndex >= emoticons.length) {
      let members = 0,
        total = 0;
      for (let i = 0; i < users.length; i++) {
        if (users[i][1] <= amounts[i]) members += 1;
        else total += amounts[i];
      }
      if (
        members > max_members ||
        (members === max_members && total > max_amounts)
      ) {
        (max_members = members), (max_amounts = total);
      }
      return;
    }

    for (const discount of [10, 20, 30, 40]) {
      const tmpAmounts = [...amounts];
      for (let i = 0; i < users.length; i++) {
        if (users[i][0] <= discount)
          amounts[i] += (emoticons[emoticonIndex] * (100 - discount)) / 100;
      }
      dfs(emoticonIndex + 1);
      amounts = [...tmpAmounts];
    }
  };
  dfs(0);
  return [max_members, max_amounts];
}
