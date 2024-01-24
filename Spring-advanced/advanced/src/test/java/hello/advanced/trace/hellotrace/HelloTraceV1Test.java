package hello.advanced.trace.hellotrace;

import static org.junit.jupiter.api.Assertions.*;

import hello.advanced.trace.TraceStatus;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class HelloTraceV1Test {


    @DisplayName("")
    @Test
    void begin_end(){
      //given
        HelloTraceV1 trace = new HelloTraceV1();

      //when
        TraceStatus status = trace.begin("hello");

      //then
        trace.end(status);
    }

    @DisplayName("")
    @Test
    void begin_exception(){
      //given

        HelloTraceV1 trace = new HelloTraceV1();
      //when
        TraceStatus status = trace.begin("hello");

      //then
        trace.exception(status,new IllegalStateException());
    }

}