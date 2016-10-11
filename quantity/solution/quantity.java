import java.util.HashMap;
import java.util.Map;
import java.lang.System;


public class Quantity {
    public Double magnitude;
    public HashMap<String, Integer> units;

    public Quantity(String unit) {
        this.magnitude = null;
        this.units = new HashMap<String, Integer>();
        this.units.put(unit, 1);
    }

    public Quantity(Double magnitude, HashMap<String, Integer> units) {
        this.magnitude = magnitude;
        this.units = units;
    }

    public Quantity(Double magnitude, String unit) {
        this.magnitude = magnitude;
        this.units = new HashMap<String, Integer>();
        this.units.put(unit, 1);
    }

    public Quantity multiply(Quantity other) {
        Double magnitude = (this.magnitude == null ? 1.0 : this.magnitude) * (other.magnitude == null ? 1.0 : other.magnitude);
        HashMap<String, Integer> units = new HashMap<String, Integer>();
        for (Map.Entry<String, Integer> entry : this.units.entrySet()) {
            Integer other_pow = other.units.get(entry.getKey());
            other_pow = other_pow == null ? 0 : other_pow;
            units.put(entry.getKey(), entry.getValue() + other_pow);
        }
        return new Quantity(magnitude, units);
    }

    public String toString() {
        return this.magnitude.toString() + " " + this.units.toString();
    }

    public static void main(String[] args) {
        Quantity q = new Quantity(3.0, "meters");
        Quantity q2 = new Quantity(4.0, "meters");
        System.out.println(q.toString() + " * " + q2.toString() + " = " + q.multiply(q2).toString());
    }
}
