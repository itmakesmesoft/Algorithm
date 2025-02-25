module.exports = {
  prompt: ({ prompter }) => {
    const domains = ["BOJ", "programmers", "SWEA", "mincoding"];
    return prompter
      .select({
        type: "input",
        name: "domain",
        message: "문제를 출제한 사이트를 선택해주세요.",
        choices: domains,
      })
      .then((answer) => {
        return { domain: answer };
      });
  },
};
