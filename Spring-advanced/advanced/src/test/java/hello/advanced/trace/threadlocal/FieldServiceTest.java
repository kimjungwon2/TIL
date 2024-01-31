package hello.advanced.trace.threadlocal;

import hello.advanced.trace.threadlocal.code.FieldService;
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
//      sleep(2000); // 동시성 문제 발생 X
        sleep(100); //동시성 문제 발생O
      threadB.start();

      //then
        sleep(3000);
        log.info("main exit");
    }

    private void sleep(int millis){
        try {
            Thread.sleep(millis);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

    }
}
