/**
 * The Inverted Stack — commitlint config.
 *
 * Mirrors the fleet's conventions but allows looser subject-case (book PRs
 * frequently quote chapter titles or proper nouns in the subject) and extends
 * the type-enum with `audio` (audiobook renders) and `pao` (PAO/Yeoman
 * editorial work) for clarity in the commit log.
 */
export default {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      ['feat', 'fix', 'docs', 'style', 'refactor', 'perf', 'test', 'build', 'ci', 'chore', 'revert', 'audio', 'pao'],
    ],
    'subject-case': [0],
    'body-leading-blank': [2, 'always'],
    'footer-leading-blank': [2, 'always'],
    'header-max-length': [2, 'always', 120],
    // Dependabot commit bodies contain long release-note URLs that exceed
    // the default 100-char body-max-line-length. Disable the rule for
    // bot-authored commits compatibility; subjects are still capped.
    'body-max-line-length': [0, 'always'],
  },
};
