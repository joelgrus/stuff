import java.util.HashMap;
import java.util.Map;
import java.lang.System;


public class Quantity {
    public Double magnitude;
    public Map<String, Integer> units;

    public Quantity(String unit) {
        this.magnitude = null;
        this.units = new HashMap<String, Integer>();
        this.units.put(unit, 1);
    }

    public Quantity(Double magnitude, Map<String, Integer> units) {
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
        Map<String, Integer> units = mergeUnits(this.units, other.units, false);
        return new Quantity(magnitude, units);
    }

    public Quantity divide(Quantity other) {
        Double magnitude = (this.magnitude == null ? 1.0 : this.magnitude) / (other.magnitude == null ? 1.0 : other.magnitude);
        Map<String, Integer> units = mergeUnits(this.units, other.units, true);
        return new Quantity(magnitude, units);
    }

    private Map<String, Integer> mergeUnits(
            Map<String, Integer> mine,
            Map<String, Integer> theirs,
            boolean dividing
        ):
        Map<String, Integer> result = new HashMap<String, Integer>();
        Set<String> allUnits = mine.keySet();
        allUnits.addAll(theirs.keySet());
        for (String unit : allUnits) {
            int total = mine.getOrDefault(unit, 0);
            if (dividing) {
                total += theirs.getOrDefault(unit, 0);
            } else {
                total -= theirs.getOrDefault(unit, 0);
            }
            if (total != 0) {
                result.put(unit, total);
            }
        }
        return result;


    public String toString() {
        return this.magnitude.toString() + " " + this.units.toString();
    }

    public static void main(String[] args) {
        Quantity q = new Quantity(3.0, "meters");
        Quantity q2 = new Quantity(4.0, "meters");
        System.out.println(q.toString() + " * " + q2.toString() + " = " + q.multiply(q2).toString());
    }
}
