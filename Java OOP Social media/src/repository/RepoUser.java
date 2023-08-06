package repository;

import domain.User;

import java.util.ArrayList;
import java.util.List;

public class RepoUser {
    private List<User> repo;

    public RepoUser(){
        this.repo = new ArrayList<>();
    }

    public List<User> getRepo() {
        return repo;
    }

    public void add(User u){
        repo.add(u);
    }

    public void remove(User u){repo.remove(u);}

    public boolean exist(int id){
        for(User u : repo)
            if(u.getId() == id)
                return true;
        return false;
    }
    public User findById(int id){
        if (exist(id))
            for (User u : repo)
                if (u.getId() == id)
                    return u;
        return new User();
    }

    public int size(){
        return repo.size();
    }
}
