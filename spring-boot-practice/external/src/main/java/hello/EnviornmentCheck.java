package hello;

import jakarta.annotation.PostConstruct;
import lombok.extern.slf4j.Slf4j;
import org.springframework.core.env.Environment;
import org.springframework.stereotype.Component;

@Slf4j
@Component
public class EnviornmentCheck {

    private final Environment env;

    public EnviornmentCheck(Environment env) {
        this.env = env;
    }

    @PostConstruct
    public void init(){
        String url = env.getProperty("url");
        String username = env.getProperty("username");
        String password = env.getProperty("password");
        log.info("env url={}",url);
        log.info("username url={}",username);
        log.info("password url={}",password);
    }

}
