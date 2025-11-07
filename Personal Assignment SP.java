import java.util.*;

class NewsArticle {
    private String title;
    private String content;
    private String author;
    private String date;

    public NewsArticle(String title, String content, String author, String date) {
        this.title = title;
        this.content = content;
        this.author = author;
        this.date = date;
    }

    public String getTitle() {
        return title;
    }

    public String getContent() {
        return content;
    }

    public String getAuthor() {
        return author;
    }

    public String getDate() {
        return date;
    }
}

class NewsSummarizer {
    public static String summarize(NewsArticle article) {
        String[] words = article.getContent().split(" ");
        int summaryLength = Math.min(words.length, 20); // Limit summary to 20 words
        StringBuilder summary = new StringBuilder();
        for (int i = 0; i < summaryLength; i++) {
            summary.append(words[i]).append(" ");
        }
        return summary.toString().trim() + "...";
    }
}

class UserInputHandler {
    public static NewsArticle getArticleFromUser() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter article title: ");
        String title = scanner.nextLine();
        System.out.print("Enter article content: ");
        String content = scanner.nextLine();
        System.out.print("Enter author name: ");
        String author = scanner.nextLine();
        System.out.print("Enter publication date: ");
        String date = scanner.nextLine();
        return new NewsArticle(title, content, author, date);
    }
}

public class Main {
    public static void main(String[] args) {
        NewsArticle article = UserInputHandler.getArticleFromUser();
        
        System.out.println("\nArticle Details:");
        System.out.println("Title: " + article.getTitle());
        System.out.println("Author: " + article.getAuthor());
        System.out.println("Date: " + article.getDate());
        System.out.println("Summary: " + NewsSummarizer.summarize(article));
    }
}
