package com.example.springtx.propagation;


import static org.assertj.core.api.AssertionsForClassTypes.assertThatThrownBy;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.UnexpectedRollbackException;

@Slf4j
@SpringBootTest
class MemberServiceTest {

    @Autowired
    MemberService memberService;
    @Autowired
    MemberRepository memberRepository;
    @Autowired
    LogRepository logRepository;

    /*
    * memberService    @Transactional: OFF
    * memberRepository @Transactional: ON
    * logRepository   @Transactional: ON
    */

    @DisplayName("")
    @Test
    void outerTxOff_success(){
      //given
        String username = "outerTxOff_success";

      //when
        memberService.joinV1(username);

      //then
        assertFalse(memberRepository.find(username).isEmpty());
    }

    @DisplayName("")
    @Test
    void outerTxOff_fail(){
        //given
        String username = "로그예외_outerTxOff_fail";

        //when
        assertThatThrownBy(()->memberService.joinV1(username))
                .isInstanceOf(RuntimeException.class);

        //then
        assertTrue(memberRepository.find(username).isPresent());
        assertTrue(logRepository.find(username).isEmpty());
    }

    /*
     * memberService    @Transactional: ON
     * memberRepository @Transactional: OFF
     * logRepository   @Transactional: OFF
     */

    @DisplayName("")
    @Test
    void singleTx(){
        //given
        String username = "singleTx";

        //when
        memberService.joinV1(username);

        //then
        assertFalse(memberRepository.find(username).isPresent());
        assertFalse(logRepository.find(username).isPresent());
    }

    /*
     * memberService    @Transactional: ON
     * memberRepository @Transactional: ON
     * logRepository   @Transactional: ON
     */

    @DisplayName("")
    @Test
    void outerTxOn_success(){
        //given
        String username = "outerTxOn_success";

        //when
        memberService.joinV1(username);

        //then
        assertFalse(memberRepository.find(username).isPresent());
        assertFalse(logRepository.find(username).isPresent());
    }

    /*
     * memberService    @Transactional: ON
     * memberRepository @Transactional: ON
     * logRepository   @Transactional: ON Exception
     */
    @DisplayName("")
    @Test
    void outerTxOn_fail(){
        //given
        String username = "로그예외_outerTxOff_fail";

        //when
        assertThatThrownBy(()->memberService.joinV1(username))
                .isInstanceOf(RuntimeException.class);

        //then: 모든 데이터가 롤백된다.
        assertTrue(memberRepository.find(username).isEmpty());
        assertTrue(logRepository.find(username).isEmpty());
    }

    /*
     * memberService    @Transactional: ON
     * memberRepository @Transactional: ON
     * logRepository   @Transactional: ON Exception
     */
    @DisplayName("")
    @Test
    void recoverException_fail(){
        //given
        String username = "로그예외_recoverException_fail";

        //when
        assertThatThrownBy(()->memberService.joinV2(username))
                .isInstanceOf(UnexpectedRollbackException.class);

        //then:
        assertTrue(memberRepository.find(username).isEmpty());
        assertTrue(logRepository.find(username).isEmpty());
    }

    /*
     * memberService    @Transactional: ON
     * memberRepository @Transactional: ON
     * logRepository   @Transactional: ON(REQUIRES_NEW) Exception
     */
    @DisplayName("")
    @Test
    void recoverException_success(){
        //given
        String username = "로그예외_recoverException_success";

        //when
        memberService.joinV2(username);

        //then: member 저장, log 롤백.
        assertTrue(memberRepository.find(username).isPresent());
        assertTrue(logRepository.find(username).isEmpty());
    }

}