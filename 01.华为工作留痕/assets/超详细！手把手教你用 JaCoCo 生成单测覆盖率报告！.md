[目录](https://www.cnblogs.com/chanshuyi/p/quick-start-of-jacoco.html#cb_post_title_url)

- [初始化项目](https://www.cnblogs.com/chanshuyi/p/quick-start-of-jacoco.html#初始化项目)
- [引入插件](https://www.cnblogs.com/chanshuyi/p/quick-start-of-jacoco.html#引入插件)
- [生成报告](https://www.cnblogs.com/chanshuyi/p/quick-start-of-jacoco.html#生成报告)
- [疑问](https://www.cnblogs.com/chanshuyi/p/quick-start-of-jacoco.html#疑问)
- [参考资料](https://www.cnblogs.com/chanshuyi/p/quick-start-of-jacoco.html#参考资料)

我们都知道 Spock 是一个单测框架，其特点是语法简明。但当我们使用 Spock 写了一堆单元测试之后，如何生成对应的单测覆盖率报告呢？一般来说，我们会使用两个插件来一起完成单测覆盖率报告的生成，分别是：

- Maven Surefire Plugin
- JaCoCo Plugin

其中 Maven Surefire Plugin 是用来在 Maven 的编译阶段运行单测代码，而 JaCoCo 则是用来生成具体的单测覆盖率报告。本文将新建一个非 Web 项目来演示如何生成 Spock 的单测覆盖率报告。

## 初始化项目

这里初始化项目一个普通的 Java 项目，并引入对应的 Spock 依赖，如下代码所示：

```xml
<!-- spock 依赖-->
<dependency>
    <groupId>org.spockframework</groupId>
    <artifactId>spock-core</artifactId>
    <version>2.0-M2-groovy-3.0</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter-engine</artifactId>
    <version>5.6.2</version>
    <scope>test</scope>
</dependency>
```

接着写一个计算器类，用于演示单测覆盖率，如下代码所示：

```java
package tech.shuyi;

public class AdvancedCalculator {
    Integer add(int a, int b) {
        return a + b;
    }

    Integer subtract(int a, int b) {
        return a - b;
    }

    Integer multi(int a, int b) {
        return a * b;
    }

    Integer divide(int a, int b) {
        return a / b;
    }
}
```

接着在 `test.groovy.tech.shuyi` 目录写一个 Groovy 单测，如下代码所示：

```groovy
package tech.shuyi

import spock.lang.Specification

class AdvancedCalculatorTest extends Specification {

    def calendar = new AdvancedCalculator()

    def "Add"() {
        expect: calendar.add(1, 2) == 3
    }

    def "Substract"() {
        expect: calendar.subtract(2, 1) == 1
    }

    def "Multi"() {
        expect: calendar.multi(2, 3) == 6
    }

    def "Divide"() {
        expect: calendar.divide(16, 4) == 4
    }
}
```

接着我们尝试运行一下单测文件，如无异常应该是成功的。

## 引入插件

在这里，我们要引入对应的两个插件，并做一些简单地配置。

首先，在 `pom.xml` 文件引入 Surefire 插件配置，如下代码所示：

```xml
<!-- surefire plugin with spock and junit -->
<plugin>
    <groupId>org.codehaus.gmavenplus</groupId>
    <artifactId>gmavenplus-plugin</artifactId>
    <version>1.9.0</version>
    <executions>
        <execution>
            <goals>
                <goal>compileTests</goal>
            </goals>
        </execution>
    </executions>
</plugin>
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.0.0-M7</version>
    <configuration>
        <!-- 配置单测失败几次后停止执行 -->
        <skipAfterFailureCount>0</skipAfterFailureCount>
        <!-- 不允许跳过单测 -->
        <skipTests>false</skipTests>
    </configuration>
</plugin>
```

接着引入 JaCoCo Plugin 的配置，如下代码所示：

```xml
<!-- JaCoCo plugin -->
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.7</version>
    <configuration>
        <includes>
            <include>tech/**/*</include>
        </includes>
    </configuration>
    <executions>
        <execution>
            <id>pre-test</id>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
        </execution>
        <execution>
            <id>post-test</id>
            <phase>test</phase>
            <goals>
                <goal>report</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

## 生成报告

做好上述报告后，直接执行 `mvn test` 就可以生成单测覆盖率报告了。如果没有什么异常的话，程序会生成单测覆盖率报告文件，地址为： `target/site/jacoco/index.html`。

我们使用浏览器打开该文件可以浏览到单测覆盖率情况，如下图所示：

![单测覆盖率报告](%E8%B6%85%E8%AF%A6%E7%BB%86%EF%BC%81%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E7%94%A8%20JaCoCo%20%E7%94%9F%E6%88%90%E5%8D%95%E6%B5%8B%E8%A6%86%E7%9B%96%E7%8E%87%E6%8A%A5%E5%91%8A%EF%BC%81.assets/image-20221020165417726.png)

## 疑问

关于如何配置这两个插件的资料很多，但都运行不起来。后面我参考了官网的配置，就成功配置好了。

- Surefire Plugin 官网文档：[Maven Surefire Plugin – Introduction](https://maven.apache.org/surefire/maven-surefire-plugin/)
- JaCoCo Plugin 官网文档：[JaCoCo - Maven Plug-in](https://www.eclemma.org/jacoco/trunk/doc/maven.html)

但对于这两个插件，我还是有一定疑问的，例如：

- 这两个插件到底都是啥作用？
- 是否一定要搭配一起使用？

通过 Surefire 插件官网，我们可以大概知道其作用为：在编译的 test 阶段，用于执行程序的单元测试，最终生成 `txt` 和 `xml` 格式的报告，存放地址为 `${basedir}/target/surefire-reports/TEST-*.xml`。

**由此可见，Surefire 的主要作用还是用于执行程序的单测程序，而不是生成报告。**当然，官网文档也说了，你可以使用 `Maven Surefire Report Plugin` 来生成 HTML 格式的报告。我根据这个文档（[Maven Surefire Report Plugin – Usage](https://maven.apache.org/surefire/maven-surefire-report-plugin/usage.html)）配置了一下 surefire-report 插件，成功地生成 HTML 格式的报告，如下图所示。

![surefire-report 插件生成的 HTML 报告](%E8%B6%85%E8%AF%A6%E7%BB%86%EF%BC%81%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E7%94%A8%20JaCoCo%20%E7%94%9F%E6%88%90%E5%8D%95%E6%B5%8B%E8%A6%86%E7%9B%96%E7%8E%87%E6%8A%A5%E5%91%8A%EF%BC%81.assets/image-20221020171048870.png)

可以看到 surefire-report 插件生成的 HTML 报告还是比较简陋的，跟 JaCoCo 插件生成的相比，显然后者更加可视化一些。

看到这里，我相信大家应该能弄明白前面两个问题了：

- 这两个插件到底都是啥作用？
- 是否一定要搭配一起使用？

简单地说，Surefire 插件主要是运行单测，生成单测数据。对于 JaCoCo 插件而言，其作用是基于 Surefire 插件去生成可视化的报告。JaCoCo 插件需要基于 Surefire 插件使用，如果去掉 Surefire 插件，JaCoCo 就生成不了报告了。