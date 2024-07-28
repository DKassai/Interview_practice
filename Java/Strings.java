package Java;
import java.util.LinkedHashSet;

public class Strings {

public static void main(String[] args) {
    String s = "hello world i have to practice java";
    String t = "hello world i dont know what to do ";
    boolean isUniqueChar = isUniqueChar(s);
    boolean isPermutation = isPermutation(s,t);
    String newString = percentString(s);
    System.out.println(isUniqueChar);
    System.out.println(isPermutation);
    System.out.println(newString);
}

static boolean isUniqueChar(String s){
    if(s.length()> 128) return false;
    
    boolean char_set[] = new boolean[128];
    for(int i = 0 ; i<s.length();i ++){
        int val = s.charAt(i);
        System.out.println(val);
        if(char_set[val]){
            return false;
        }   
        char_set[val] = true;
    }
    return true;
}

static boolean isPermutation(String s, String t){
    if(s.length()!= t.length()) return false;

    int[] letters = new int[128];

    for(int i = 0 ; i<s.length();i ++){
        letters[s.charAt(i)]++;
    }
    for(int i =0; i<t.length();i ++){
        letters[t.charAt(i)]--;
        if(letters[t.charAt(i)]<0){
            return false;
        }
    }
    return true;
}

static String isPermutationofPalindrom(String s){
    s = s.toLowerCase().replaceAll("[^a-zA-Z]", "");
    LinkedHashSet<Character> set = new LinkedHashSet<>();

    for(char c: s.toCharArray()){
        set.add(c);
    }
}
