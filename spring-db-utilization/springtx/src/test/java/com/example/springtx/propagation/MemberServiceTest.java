package com.example.springtx.propagation;

import static org.junit.jupiter.api.Assertions.*;

import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

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
}