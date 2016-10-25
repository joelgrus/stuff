import java.lang.System;

public class Quantity {

    public static void main(String[] args) {
        // multiplication
        Quantity q1 = new Quantity(3.0, "meters");
        Quantity q2 = new Quantity(4.0, "meters");
        Quantity answer = q1.multiply(q2);
        System.out.println(q1.toString() + " * " + q2.toString() + " = " + answer.toString());

        // division
        Quantity requests = new Quantity(70000, "requests");
        Quantity seconds = new Quantity(3600, "seconds");
        Quantity answer = requests.divide(seconds);
        System.out.println(requests.toString() + " / " + seconds.toString() + " = " + answer.toString());
    }
    // division, addition/subtraction, exponentiation, ...
}
