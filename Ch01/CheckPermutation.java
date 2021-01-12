import java.util.*;

public class CheckPermutation {
	
	public static boolean checkPermutation(String str1, String str2) {
		if (str1.length() != str2.length()) 
			return false;
		
		Hashtable<Character, Integer> table = new Hashtable<>();
		for (int i = 0; i < str1.length(); i++) {
			char ch = str1.charAt(i);
			if (!table.containsKey(ch)) 
				table.put(ch, 1);
			else 
				table.put(ch, table.get(ch) + 1);
		}
		for (int i = 0; i < str2.length(); i++) {
			char ch = str2.charAt(i);
			if (!table.containsKey(ch) || table.get(ch) < 0) 
				return false;
			table.put(ch, table.get(ch) - 1);
		}
		return true;
	}

	public static String sort(String str) {
		char[] content = str.toCharArray();
		Arrays.sort(content);
		return new String(content);
	}

	public static boolean checkPermutation2(String str1, String str2) {
		if (str1.length() != str2.length())
			return false;
		return sort(str1).equals(sort(str2));
	}

	public static void main(String[] args) {
		String[][] dataT = {{"abcd", "bacd"}, {"wef34f", "wffe34"}};
		for (String[] pair : dataT) {
			String word1 = pair[0];
			String word2 = pair[1];
			boolean result = checkPermutation(word1, word2);
			System.out.println(word1 + ", " + word2 + ": " + result);
		}
	}

}
