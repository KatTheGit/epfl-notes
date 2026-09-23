class Poly2 {
    // solves a polynomial of the form ax² + bx + c
    public static void main(String[] args) {
        //System.out.println("Hello");
        
        String aStr = args[0];
        String bStr = args[1];
        String cStr = args[2];
        
        double a = Double.parseDouble(aStr);
        double b = Double.parseDouble(bStr);
        double c = Double.parseDouble(cStr);
        //System.out.printf("Coefficients chosen: a: %d, b:%d, c:%d.", a, b, c);
        System.out.println("Coefficients chosen: a: " + a + ", b: " + b + ", c: " + c + ".");

        double delta = Math.pow(b, 2) - 4.0 * a * c;
        System.out.println("Delta: " + delta + ".");

        if (delta < 0.0) {
            System.out.println("There is no real solution.");
        }
        else if (delta == 0.0) {
            double solution = -b / (2.0 * a);
            System.out.println("The solution is: " + solution + ".");
        }
        else {
            double solution_1 = (-b - Math.sqrt(delta)) / (2.0 * a);
            double solution_2 = (-b + Math.sqrt(delta)) / (2.0 * a);

            System.out.println("The two solutions are " + solution_1 + " and " + solution_2 + ".");
        }
    }
}
