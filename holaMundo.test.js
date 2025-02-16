// holaMundo.test.js
const holaMundo = require('./holamundo');

test('Debe devolver "Hola Mundo"', () => {
    expect(holaMundo()).toBe("Hola Mundo");
});