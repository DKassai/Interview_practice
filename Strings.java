public class Strings {

public static void main(String[] args) {
    String s = "hello world i have to practice java";
    boolean isUniqueChar = isUniqueChar(s);
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
}
