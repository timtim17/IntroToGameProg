def quadraticFormula(a, b, c):
    from cmath import sqrt
    numberSq = sqrt(b ** 2 - 4 * a * c)
    if numberSq.imag == 0:
        numberSq =  numberSq.real
    elif numberSq.real == 0:
        numberSq = numberSq.imag * 1j
    return [(-b + numberSq)/(2 * a),
            (-b - numberSq)/(2 * a)]

answers = quadraticFormula(4, 5, -2)
print "The solution set is: {" + str(answers[0]) + ", " + str(answers[1]) + "}"

answers = quadraticFormula(1, 1, 500)
print "The solution set is: {" + str(answers[0]) + ", " + str(answers[1]) + "}"
