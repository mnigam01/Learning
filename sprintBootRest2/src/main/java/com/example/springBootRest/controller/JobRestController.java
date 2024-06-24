package com.example.springBootRest.controller;

import com.example.springBootRest.model.JobPost;
import com.example.springBootRest.service.JobService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
//@CrossOrigin(origins = "https://www.go.com")
public class JobRestController {

    @Autowired
    private JobService service;


    @GetMapping("jobPosts")
    public List<JobPost> getAllJobs() {
        return service.getAllJobs();

    }
    @GetMapping("jobPost/{postId}")
    public JobPost getJobPost(@PathVariable int postId){
        return service.getJobPost(postId);
    }

    @PostMapping("jobPost")
    public void addJob(@RequestBody JobPost jobPost){
        service.addJobPost(jobPost);
    }

    @PutMapping("jobPost")
    public void updateJob(@RequestBody JobPost jobPost){
        service.updateJobPost(jobPost);
    }


//    @DeleteMapping("jobPost/{id}")
    @DeleteMapping("jobPost")
    public void deleteJob(@RequestBody JobPost jobPost){
        service.deleteJobPost(jobPost);
    }

    @GetMapping("jobPost/keyword/{keyword}")
    public List<JobPost> searchByKeyword(@PathVariable String keyword){
        return service.searchByKeyword(keyword);
    }


}
