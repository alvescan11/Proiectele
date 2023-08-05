package org.example.domain;

import java.util.Objects;
import java.util.UUID;

public class User extends Entity<UUID> {
    private String userName;
    private String password;
    public User() {
    }

    public User(String userName, String pword) {
        this.userName = userName;
        this.password = pword;
    }
    public String getUserName() {
        return userName;
    }
    public void setUserName(String userName) {
        this.userName = userName;
    }
    public String getPassword() {
        return password;
    }
    public void setPassword(String password) {
        this.password = password;
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return Objects.equals(userName, user.userName) && Objects.equals(password, user.password);
    }
    @Override
    public int hashCode() {
        return Objects.hash(userName, password);
    }


}
