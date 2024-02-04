function
getValue(a, b)
{
return 3 * a + 2 * b;
}

describe("getValue(a, b) function", function()
{
    it("should be equal", function()
{
    expect(getValue(1, 2)).toBe(7);
});

it("should be equal", function()
{
    expect(getValue(7, 4)).toBe(29);
});
});
