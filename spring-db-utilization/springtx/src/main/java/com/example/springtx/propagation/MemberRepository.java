package com.example.springtx.propagation;

import jakarta.persistence.EntityManager;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;
import java.util.*;

@Slf4j
@Repository
@RequiredArgsConstructor
public class MemberRepository {

    private final EntityManager em;

    @Transactional
    public void save(Member member){
        log.info("member 저장");
        em.persist(member);
    }

    public Optional<Member> find(String username){
        log.info("Member find 시작");
        return em.createQuery("select m from Member m where m.username =:username",Member.class)
                .setParameter("username",username)
                .getResultList().stream().findAny();
    }


}
