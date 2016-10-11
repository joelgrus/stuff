import java.lang.System;

public class Quantity {

    public static void main(String[] args) {
        Quantity q1 = new Quantity(3.0, "meters");
        Quantity q2 = new Quantity(4.0, "meters");
        Quantity answer = q1.multiply(q2)
        System.out.println(q1.toString() + " * " + q2.toString() + " = " + answer.toString());
    }
    // division, addition/subtraction, exponentiation, ...
}
