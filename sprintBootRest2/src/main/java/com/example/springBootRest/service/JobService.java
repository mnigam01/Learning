package com.example.springBootRest.service;

import com.example.springBootRest.model.JobPost;
import com.example.springBootRest.repo.JobRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class JobService {
    @Autowired
    private JobRepo repo;

    public List<JobPost> getAllJobs(){
        return repo.findAll();
    }
    public void addJobPost(JobPost post){
        repo.save(post);
    }

    public JobPost getJobPost(int postId) {
        return repo.findById(postId).orElse(new JobPost());
    }

    public void updateJobPost(JobPost jobPost) {
        repo.save(jobPost);
    }

    public void deleteJobPost(JobPost jobPost) {
        repo.delete(jobPost);
//        repo.deleteById(postId);
    }

    public List<JobPost> searchByKeyword(String keyword) {
        return  repo.findByPostProfileContainingOrPostDescContaining(keyword, keyword);
    }
}
