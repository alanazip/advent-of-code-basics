// sum.js
function sum(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new Error('Arguments must be numbers');
  }
  return a + b;
}

module.exports = sum;

// sum.test.js
const sum = require('./sum');

describe('sum function', () => {
  test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
  });

  test('adds -1 + 2 to equal 1', () => {
    expect(sum(-1, 2)).toBe(1);
  });

  test('throws error when arguments are not numbers', () => {
    expect(() => sum('1', 2)).toThrow('Arguments must be numbers');
    expect(() => sum(1, 'a')).toThrow('Arguments must be numbers');
  });
});