package hello.advanced.trace.logtrace;

import hello.advanced.trace.TraceStatus;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

public class ThreadLogTraceTest {

    ThreadLocalLogTrace trace = new ThreadLocalLogTrace();

    @DisplayName("")
    @Test
    void begin_end_level2(){
      //given
        TraceStatus status1= trace.begin("hello1");
        TraceStatus status2= trace.begin("hello2");
        trace.end(status2);
        trace.end(status1);

        //when

    }

    @DisplayName("")
    @Test
    void begin_exception_level2(){
        //given
        TraceStatus status1= trace.begin("hello1");
        TraceStatus status2= trace.begin("hello2");
        trace.exception(status2,new IllegalStateException());
        trace.exception(status1,new IllegalStateException());

        //when

    }

}
