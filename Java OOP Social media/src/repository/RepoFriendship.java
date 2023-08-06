package repository;

import domain.Friendship;

import java.util.ArrayList;
import java.util.List;

public class RepoFriendship {
    private List<Friendship> repo;

    public RepoFriendship(){
        this.repo = new ArrayList<>();
    }

    public List<Friendship> getRepo() {
        return repo;
    }


    public void add(Friendship f){
        repo.add(f);
    }

    public void remove(Friendship f){
        repo.remove(f);
    }

    public boolean exist(int id){
        for (Friendship f : repo)
            if (f.getId() == id)
                return true;
        return false;
    }
    public Friendship findById(int id){
        if (exist(id))
            for (Friendship f : repo)
                if (f.getId() == id)
                    return f;
        return new Friendship();
    }

    public int size(){
        return repo.size();
    }

    public boolean isFriendWith(int idFriendship, int idFriend){
        Friendship fr = findById(idFriendship);
        for(int id : fr.getFriends())
            if (id == idFriend)
                return true;
        return false;
    }
}
