import java.lang.System;


public class Quantity {

    public static void main(String[] args) {
        Quantity q = new Quantity(3.0, "meters");
        Quantity q2 = new Quantity(4.0, "meters");
        System.out.println(q.toString() + " * " + q2.toString() + " = " + q.multiply(q2).toString());
    }
    // division, addition, exponentation, ...
}
