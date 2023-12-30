package hello.external;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Map;
import lombok.extern.slf4j.Slf4j;

@Slf4j
class OsEnvTest {

    public static void main(String[] args){
        Map<String, String> envMap = System.getenv();
        for (String key : envMap.keySet()) {
            log.info("env {}={}",key,System.getenv(key));
        }
    }
}