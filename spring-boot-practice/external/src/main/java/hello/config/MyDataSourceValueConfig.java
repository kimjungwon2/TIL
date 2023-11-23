package hello.config;

import hello.datasource.MyDataSource;
import java.time.Duration;
import java.util.List;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Slf4j
@Configuration
public class MyDataSourceValueConfig {

    @Value("${my.datasource.url}")
    private String url;
    @Value("${my.datasource.username}")
    private String username;
    @Value("${my.datasource.password}")
    String password;
    @Value("${my.datasource.etc.max-connection}")
    int maxConnection;
    @Value("${my.datasource.etc.timeout}")
    Duration timeout;
    @Value("${my.datasource.etc.options}")
    List<String> options;

    @Bean
    public MyDataSource myDataSource1(){
        return new MyDataSource(url,username, password,maxConnection,timeout,options);
    }
}
