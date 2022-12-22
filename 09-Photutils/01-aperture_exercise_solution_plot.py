plt.figure(figsize=(5, 5))
norm = simple_norm(data, 'sqrt', percent=99.0)
plt.imshow(data, norm=norm)
patches = aper.plot(color='orange', lw=2)
