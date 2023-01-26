package hello.core.member;

public class Member {

    private Long id;
    private String name;
    private Grade grade;

    public Member(Long id, String name, Grade gradle) {
        this.id = id;
        this.name = name;
        this.grade = gradle;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setGradle(Grade gradle) {
        this.grade = gradle;
    }

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public Grade getGradle() {
        return grade;
    }
}
