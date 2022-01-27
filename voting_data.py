# The variables below represent the percentages of democratic votes in Pennsylvania and Ohio (one value for each state).
dem_share_PA = [60.08, 40.64, 36.07, 41.21, 31.04, 43.78, 44.08, 46.85, 44.71, 46.15, 63.10, 52.20, 43.18, 40.24, 39.92, 47.87, 37.77, 40.11, 49.85, 48.61, 38.62, 54.25, 34.84, 47.75, 43.82, 55.97, 58.23, 42.97, 42.38, 36.11, 37.53, 42.65, 50.96, 47.43, 56.24, 45.60, 46.39, 35.22, 48.56, 32.97, 57.88, 36.05, 37.72, 50.36, 32.12, 41.55, 54.66, 57.81, 54.58, 32.88, 54.37, 40.45, 47.61, 60.49, 43.11, 27.32, 44.03, 33.56, 37.26, 54.64, 43.12, 25.34, 49.79, 83.56, 40.09, 60.81, 49.81]
dem_share_OH = [56.94, 50.46, 65.99, 45.88, 42.23, 45.26, 57.01, 53.61, 59.10, 61.48, 43.43, 44.69, 54.59, 48.36, 45.89, 48.62, 43.92, 38.23, 28.79, 63.57, 38.07, 40.18, 43.05, 41.56, 42.49, 36.06, 52.76, 46.07, 39.43, 39.26, 47.47, 27.92, 38.01, 45.45, 29.07, 28.94, 51.28, 50.10, 39.84, 36.43, 35.71, 31.47, 47.01, 40.10, 48.76, 31.56, 39.86, 45.31, 35.47, 51.38, 46.33, 48.73, 41.77, 41.32, 48.46, 53.14, 34.01, 54.74, 40.67, 38.96, 46.29, 38.25, 6.80, 31.75, 46.33, 44.90, 33.57, 38.10, 39.67, 40.47, 49.44, 37.62, 36.71, 46.73, 42.20, 53.16, 52.40, 58.36, 68.02, 38.53, 34.58, 69.64, 60.50, 53.53, 36.54, 49.58, 41.97, 38.11]

import numpy as np

def bootstrap_mean_ci(sample, sample_size, n_bootstraps, ci):
	# <---INSERT YOUR CODE HERE--->
  bootstrap = np.array([np.random.choice(sample, sample_size, replace = True) for _ in range(n_bootstraps)])
  data_mean = np.mean(bootstrap)
  lower = np.mean(np.percentile(bootstrap, (100-ci)/2, axis = 1))
  lower_sd = np.std(np.percentile(bootstrap, (100-ci)/2, axis = 1))
  upper = np.mean(np.percentile(bootstrap, 100-(100-ci)/2,  axis = 1))
  upper_sd = np.std(np.percentile(bootstrap, 100-(100-ci)/2,  axis = 1))
  return data_mean, lower, upper, lower_sd, upper_sd

def permut_test(sample1, sample2, n_permutations):
  """
  sample1: 1D array
  sample2: 1D array (note that the size of the two arrays can be different)
  n_permutations: number of permutations to calculate the p-value
  """
  k = 0
  result_list = []
  concat = np.concatenate([sample1, sample2])
  for i in range(n_permutations):
      perm = np.random.permutation(concat)
      pold = perm[:int(len(perm)/2)]
      pnew = perm[int(len(perm)/2):]
      result_list.append(np.abs(np.mean(pnew) - np.mean(pold)))
  result_list = np.asarray(result_list)
  lower = np.percentile(result_list, 0.5)
  upper = np.percentile(result_list, 99.5)
  k += np.sum(result_list >= upper, axis = 0)
  k += np.sum(result_list <= lower, axis = 0)
  pvalue = k/n_permutations
  return pvalue

p = permut_test(dem_share_PA, dem_share_OH, 10000)
print(p)