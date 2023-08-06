package domain;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Friendship {
    private int id;
    private List<Integer> friends;
    public Friendship(int id, List<Integer> friends) {
        this.id = id;
        this.friends = friends;
    }

    public Friendship(){
        this.id = 0;
        this.friends = new ArrayList<Integer>();
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Integer> getFriends() {
        return friends;
    }

    public void setFriends(List<Integer> friends) {
        this.friends = friends;
    }

    @Override
    public String toString() {
        return "Friendship{" +
                "id=" + id +
                ", friends=" + friends +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Friendship that = (Friendship) o;
        return id == that.id && Objects.equals(friends, that.friends);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, friends);
    }

    public void addFriend(int id){
        this.friends.add(id);
    }

    public void removeFriend(int id){
        for(int i = 0; i < friends.size();i++)
            if (friends.get(i) == id) {
                int index = i;
                i = friends.size();
                friends.remove(index);
            }
    }
}
