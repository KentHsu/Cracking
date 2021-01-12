public class URLify {

	public static void urlify(char[] content, int length) {
		int idx = content.length;
		for (int i = length - 1; i >= 0; i--) {
			if (content[i] == ' ') {
				content[idx - 3] = '%';
				content[idx - 2] = '2';
				content[idx - 1] = '0';
				idx -= 3;
			} else {
				content[idx - 1] = content[i];
				idx -= 1;
			}
		}
	}

	public static void main(String[] args) {
		char[] word = "Mr John Smith    ".toCharArray();
		int truelength = 13;
		urlify(word, truelength);
		System.out.println(word);
	}
}
