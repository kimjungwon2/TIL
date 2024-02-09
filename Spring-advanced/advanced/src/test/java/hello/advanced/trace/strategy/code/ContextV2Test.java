package hello.advanced.trace.strategy.code;

import hello.advanced.trace.strategy.code.strategy.ContextV1;
import hello.advanced.trace.strategy.code.strategy.ContextV2;
import hello.advanced.trace.strategy.code.strategy.Strategy;
import hello.advanced.trace.strategy.code.strategy.StrategyLogic1;
import hello.advanced.trace.strategy.code.strategy.StrategyLogic2;
import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

@Slf4j
public class ContextV2Test {

    @DisplayName("")
    @Test
    void startegyV1(){
      //given
        ContextV2 context = new ContextV2();
        context.execute(new StrategyLogic1());
        context.execute(new StrategyLogic2());
    }

    @DisplayName("전략 패턴 익명 내부 클래스")
    @Test
    void startegyV2(){
        //given
        ContextV2 context = new ContextV2();
        context.execute(new Strategy(){
            @Override
            public void call() {
                log.info("비즈니스 로직1 실행");
            }
        });

        context.execute(new Strategy(){
            @Override
            public void call() {
                log.info("비즈니스 로직2 실행");
            }
        });
    }

    @DisplayName("전략 패턴 익명 내부 클래스2, 람다")
    @Test
    void startegyV3(){
        //given
        ContextV2 context = new ContextV2();
        context.execute(()->log.info("비즈니스 로직1 실행"));
        context.execute(()->log.info("비즈니스 로직2 실행"));
    }



}
