# hep-faas
high energy physics functions as a service (based on OpenFaaS)


# Deploy Black-Box function and Bayesian Optimization Driver
```
faas-cli deploy -f blackboxfunc.yml
kubectl create -f jupyter
```

# Run

* connect to the Notebook server and run

```
kubectl logs -l app=jupyter 
open http://localhost:31313/notebooks/BlackBox.ipynb
```
