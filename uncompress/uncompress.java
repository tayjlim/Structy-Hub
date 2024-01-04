class Source {
  public static String uncompress(String s) {
    String result = "";
    String numbers = "0123456789";
    int i = 0;
    int j = 0;
    while (j < s.length()) {
      System.out.println(numbers.contains(String.valueOf(s.charAt(j))));
      if (numbers.contains(String.valueOf(s.charAt(j))) == true) {//if we hit we add to j
       
        j += 1;
        System.out.println(j + " this is j");
      } else {// if we hit a char
        int num = Integer.parseInt(s.substring(i, j));
        System.out.println(num + " this is num");
        
          for (int count = 0; count < num; count += 1) {
            result += s.charAt(j);
          }
        j += 1;
        i = j;
        System.out.println(i + " this is i");
​
        
      }
    }
    return result;
  }
​
  public static void run() {
    // this function behaves as `main()` for the 'run' command
    // you may sandbox in this function, but should not remove it
    Source.uncompress("2c3a1t"); // -> "ccaaat"
  }
}  