def JobScheduling(self,Jobs,n):
        
        # code edutechbarsha
        # Sorting jobs based on profit in descending order
        Jobs.sort(key=lambda x: x.profit, reverse=True)

        # Find maximum deadline to define the size of the time slots array
        max_deadline = max(job.deadline for job in Jobs)
        
        # Array to track which slots are filled
        time_slots = [-1] * (max_deadline + 1)  # using max_deadline + 1 for 1-based index

        total_jobs = 0
        total_profit = 0
        
        # Iterating over each job
        for job in Jobs:
            # Finding a slot for the job
            for j in range(min(max_deadline, job.deadline), 0, -1):
                if time_slots[j] == -1:  # If slot is empty
                    time_slots[j] = job.id
                    total_jobs += 1
                    total_profit += job.profit
                    break
        
        return total_jobs, total_profit
