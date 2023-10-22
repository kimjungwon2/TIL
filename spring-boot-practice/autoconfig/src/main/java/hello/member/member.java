package hello.member;

import lombok.Data;

@Data
public class member {

    private String memberId;
    private String name;

    public member() {
    }

    public member(String memberId, String name) {
        this.memberId = memberId;
        this.name = name;
    }
}
