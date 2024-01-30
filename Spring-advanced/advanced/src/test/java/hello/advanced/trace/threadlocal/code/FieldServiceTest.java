package hello.advanced.trace.threadlocal.code;

import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

@Slf4j
public class FieldServiceTest {

    private FieldService fieldService = new FieldService();

    @DisplayName("")
    @Test
    void field(){
      log.info("main start");
      Runnable userA = () ->{
          fieldService.logic("userA");
      };
      Runnable userB = () ->{
            fieldService.logic("userB");
      };

      Thread threadA = new Thread(userA);
      threadA.setName("thread-A");
      Thread threadB = new Thread(userB);
      threadB.setName("thread-B");

      //when
      threadA.start();
      sleep(2000);
      threadB.start();

      //then
    }

    private void sleep(int millis){
        try {
            Thread.sleep(millis);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

    }
}
