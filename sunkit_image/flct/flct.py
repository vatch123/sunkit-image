import numpy as np

try:
    from sunkit_image.flct import _pyflct
except ImportError:
    _pyflct = None

__all__ = ["flct",
           "read_2_images",
           "read_3_images",
           "write_2_images",
           "write_3_images",
           "column_row_of_two",
           "column_row_of_three"]


def read_2_images(filename, order="row"):
    """
    Reads two arrays of the same size from a ``dat`` file.

    .. note ::
        This function can be used to read only special arrays which were written
        using the ``write`` functions in `~sunkit_image.flct` or the IDL IO routines
        as given on the FLCT `website <http://solarmuri.ssl.berkeley.edu/~fisher/public/software/FLCT/C_VERSIONS/>`__.

    Parameters
    ----------
    filename : `str`
        The name of ``dat`` file.
    order : {"row" | "column"}
        The order in which the array elements are stored that is whether they are stored as row
        major or column major.

    Returns
    -------
    `tuple`
        A tuple containing two `~numpy.ndarray`.
    """

    # Checking whether the C extension is correctly built.
    if _pyflct is None:
        raise ImportError("C extension for flct is missing, please rebuild.")

    if order.lower() not in ["row", "column"]:
        raise ValueError("The order of the arrays is not correctly specified. It can only be 'row' or 'column'")

    if order is "row":
        transp = 0
    else:
        transp = 1

    ier, a, b = _pyflct.read_two_images(filename, transp)

    if ier is not 1:
        raise ValueError("The file was not read correctly. Please check the file.")

    else:
        return a, b


def read_3_images(filename, order="row"):
    """
    Read three arrays of the same size from a ``dat`` file.

    .. note ::
        This function can be used to read only special arrays which were written
        using the ``write`` functions in `~sunkit_image.flct` or the IDL IO routines
        as given on the FLCT source `website <http://solarmuri.ssl.berkeley.edu/~fisher/public/software/FLCT/C_VERSIONS/>`__.

    Parameters
    ----------
    filename : `str`
        The name of ``dat`` file.
    order : {"row" | "column"}
        The order in which the array elements are stored that is whether they are stored as row
        major or column major.

    Returns
    -------
    `tuple`
        A tuple containing three `~numpy.ndarray`.
    """

    # Checking whether the C extension is correctly built.
    if _pyflct is None:
        raise ImportError("C extension for flct is missing, please rebuild.")

    if order.lower() not in ["row", "column"]:
        raise ValueError("The order of the arrays is not correctly specified. It can only be 'row' or 'column'")

    if order is "row":
        transp = 0
    else:
        transp = 1

    ier, a, b, c = _pyflct.read_three_images(filename, transp)

    if ier is not 1:
        raise ValueError("The file was not read correctly. Please check the file")

    else:
        return a, b, c


def write_2_images(filename, array1, array2, order="row"):
    """
    Write two arrays of the same size to a ``dat`` file.

    Parameters
    ----------
    filename : `str`
        The name of ``dat`` file.
    array1 : `numpy.ndarray`
        The first array to be stored.
    array2 : `numpy.ndarray`
        The second array to be stored.
    order : {"row" | "column"}
        The order in which the array elements are stored that is whether they are stored as row
        major or column major.

    Returns
    -------
    A dat file of the ``filename`` is created in the current directory without returning anything.
    """

    # Checking whether the C extension is correctly built.
    if _pyflct is None:
        raise ImportError("C extension for flct is missing, please rebuild.")

    if order.lower() not in ["row", "column"]:
        raise ValueError("The order of the arrays is not correctly specified. It can only be 'row' or 'column'")

    if order is "row":
        transp = 0
    else:
        transp = 1

    ier = _pyflct.write_two_images(filename, array1, array2, transp)

    if ier is not 1:
        raise ValueError("The file was not read correctly. Please check the file")


def write_3_images(filename, array1, array2, array3, order="row"):
    """
    Write three arrays of the same size to a ``dat`` file.

    Parameters
    ----------
    filename : `string`
        The name of ``dat`` file.
    array1 : `numpy.ndarray`
        The first array to be stored.
    array2 : `numpy.ndarray`
        The second array to be stored.
    array3 : `numpy.ndarray`
        The third array to be stored.
    order : {"row" | "column"}
        The order in which the array elements are stored that is whether they are stored as row
        major or column major.

    Returns
    -------
    A dat file of the ``filename`` is created in the current directory without returning anything.
    """

    # Checking whether the C extension is correctly built.
    if _pyflct is None:
        raise ImportError("C extension for flct is missing, please rebuild.")

    if order.lower() not in ["row", "column"]:
        raise ValueError("The order of the arrays is not correctly specified. It can only be 'row' or 'column'")

    if order is "row":
        transp = 0
    else:
        transp = 1

    ier = _pyflct.write_three_images(filename, array1, array2, array3, transp)

    if ier is not 1:
        raise ValueError("The file was not read correctly. Please check the file")


def column_row_of_two(array1, array2):
    """
    Takes two arrays and swaps the order in which they were stored i.e. changing
    from column major to row major and **not** the vice-versa. This may change the values stored in
    the array as the arrays are first converted to a binary format and then the order change takes
    place.

    Parameters
    ----------
    array1 : `numpy.ndarray`
        The first array whose order is to be changed.
    array2 : `numpy.ndarray`
        The second array whose order is to be changed.

    Returns
    -------
    `tuple`
        It returns the two input arrays after changing their order from column major to
        row major.
    """

    # Checking whether the C extension is correctly built.
    if _pyflct is None:
        raise ImportError("C extension for flct is missing, please rebuild.")

    one, two = _pyflct.swap_order_two(array1, array2)

    return (one, two)


def column_row_of_three(array1, array2, array3):
    """
    Takes three arrays and swaps the order in which they were stored i.e. changing
    from column major to row major and **not** the vice-versa. This may change the values stored in
    the array as the arrays are first converted to a binary format and then the order change takes
    place.

    Parameters
    ----------
    array1 : `numpy.ndarray`
        The first array whose order is to be changed.
    array2 : `numpy.ndarray`
        The second array whose order is to be changed.
    array3 : `numpy.ndarray`
        The third array whose order is to be changed.

    Returns
    -------
    `tuple`
        It returns the two input arrays after changing their order from column major to
        row major.
    """

    # Checking whether the C extension is correctly built.
    if _pyflct is None:
        raise ImportError("C extension for flct is missing, please rebuild.")

    one, two, three = _pyflct.swap_order_three(array1, array2, array3)

    return (one, two, three)


def flct(
    image1,
    image2,
    order,
    deltat,
    deltas,
    sigma,
    quiet=False,
    biascor=False,
    thresh=0.0,
    absflag=False,
    skip=None,
    poff=0,
    qoff=0,
    interp=False,
    kr=None,
    pc=False,
    latmin=0,
    latmax=0.2,
):
    """
    Performs Fourier Local Correlation Tracking by calling the FLCT C library.
    

    .. note::

        * In the references there are some dat files which can be used to test the FLCT code. The
          best method to read those dat files is the `sunkit_image.flct.read_2_images` and
          `sunkit_image.flct.read_3_images` as the arrays would automatically be read in row major
          format.
        * If you use the IDL IO routines to get the input arrays from ``dat`` files,
          the IDL routines always read the binary files in the column major, but both Python and C,
          on which these functions are written are row major so the order of the arrays have to be
          changed which can be done with the ``order`` keyword. This may lead to different values
          in both the cases.
        * If your input arrays are column major then pass the `order` parameter as `column` and it
          will automatically take care of the order change. But this can produce some changes in
          the values of the arrays.

    Parameters
    ----------
    image1 : `numpy.ndarray`
        The first image.
    image2 : `numpy.ndarray`
        The second image taken after ``deltat`` time of the first one.
    order : {"row" | "column"}
        The order in which the array elements are stored that is whether they are stored as row
        major or column major.
    deltat : `float`
        The time interval between the two images.
    deltas : `float`
        Units of length of the side of a single pixel. Velocity is computed in units of ``deltas``/``deltat``.
    sigma : `float`, optional
        The width of Gaussian kernel with which the images are to be modulated. Sub-images are weighted
        by Gaussian of width sigma. If sigma is ``0`` then the overall shift between the images is
        returned.
    quiet : `bool`, optional
        If set to `True` all the error messages of FLCT C code will be suppressed.
        Defaults to `False`.
    biascor : `bool`, optional
        If set to `True` bias correction will be applied while computing the velocities.
        This bias is intrinsic to the FLCT algorithm and can underestimate the velocities
        during calculations. For more
        details visit `here <http://solarmuri.ssl.berkeley.edu/~fisher/public/software/FLCT/C_VERSIONS/flct_1.06/doc/bias_correction_in_flct.txt>`__.
    thresh : `float`, optional
        A calculation will not be done for a pixel if the average absolute value
        between the two images is less than ``thresh``.
        If ``thresh`` is between 0 and 1, ``thresh`` is assumed given in
       in relative units of the maximum absolute pixel value in the average of the two images.
        Defaults to 0.
    absflag : `bool`, optional
        This is set to `True` to force the ``thresh`` values between 0 and 1 to be considered in
        absolute terms.
        Defaults to False.
    skip : `int`, optional
        The number of pixels to be skipped in the ``x`` and ``y`` direction after each calculation of a
        velocity for a pixel.
        Defaults to `None`.
    poff : `int`, optional
        The offset in "x" direction after ``skip`` is enabled.
        Defaults to 0.
    qoff : `int`, optional
        The offset in "y" direction after ``skip`` is enabled.
        Defaults to 0.
    interp : `bool`, optional
        If set to `True` interpolation will be performed at the skipped pixels.
        Defaults to `False`.
    kr : `float`, optional
        Apply a low-pass filter to the sub-images, with a Gaussian of a characteristic wavenumber
        that is a factor of ``kr`` times the largest possible wave numbers in "x", "y" directions.
        ``kr`` should be positive. 
        Defaults to `None`
    pc : `bool`, optional
        Set to `True` if the images are Plate Carrée projected.
        Defaults to `False`.
    latmin : `float`, optional
        Lower latitude limit in radians, used with ``pc``.
        Defaults to 0.
    latmax : `float`, optional
        Upper latitude limit in radians, used with ``pc``.
        Defaults to 0.2.

    Returns
    -------
    `tuple`
        A tuple containing the velocity `~numpy.ndarray` in the following order ``vx``, ``vy``, and ``vm``.
        ``vx`` is the velocity at every pixel location in the ``x`` direction.
        ``vy`` is the velocity at every pixel location in the ``y`` direction.
        ``vm`` is the mask array which is set to 1 at pixel locations where the FLCT calculations
        were performed, 0 where the calculations were not performed and 0.5 where the results were
        interpolated.

    References
    ----------
    * The FLCT software package which can be found `here <http://solarmuri.ssl.berkeley.edu/~fisher/public/software/FLCT/C_VERSIONS/>`__.
    """

    # Checking whether the C extension is correctly built.
    if _pyflct is None:
        raise ImportError("C extension for flct is missing, please rebuild.")

    if order.lower() not in ["row", "column"]:
        raise ValueError("The order of the arrays is not correctly specified. It can only be 'row' or 'column'")

    # If order is column then order swap is performed.
    if order is "column":
        image1, image2 = column_row_of_two(image1, image2)
        image1 = np.array(image1)
        image2 = np.array(image2)

    if quiet is True:
        verbose = 0
    else:
        verbose = 1

    if biascor is False:
        biascor = 0
    else:
        biascor = 1

    if absflag is False:
        absflag = 0
    else:
        absflag = 1

    if interp is False:
        interp = 0
    else:
        interp = 1

    if skip is not None:
        if skip <= 0:
            raise ValueError("Skip value must be greater than zero.")
        skipon = skip + np.abs(qoff) + np.abs(poff)

        if np.abs(poff) >= skip or np.abs(qoff) >= skip:
            raise ValueError("The absolute value of 'poff' and 'qoff' must be less than skip.")
    else:
        skip = 0
        skipon = 0

    if kr is not None:
        if kr <= 0.0 or kr >= 20.0:
            raise ValueError("The value of 'kr' must be between 0 and 20.")
        filter = 1
    else:
        kr = 0.0
        filter = 0

    if(poff < 0):
        poff = skip - np.abs(poff)
    if(qoff < 0):
        qoff = skip - np.abs(qoff)

    nx = image1.shape[0]
    ny = image2.shape[1]

    if sigma == 0:
        nx = 1
        ny = 1

    if skip is not None:
        if skip >= nx or skip >= ny:
            raise ValueError("Skip is greater than the input dimensions")

    # This takes care of the order transformations in the C code.
    transp = 1

    vx = np.zeros((nx * ny,), dtype=float)
    vy = np.zeros((nx * ny,), dtype=float)
    vm = np.zeros((nx * ny,), dtype=float)

    if pc is True:
        ierflct, vx_c, vy_c, vm_c = _pyflct.pyflct_plate_carree(
            transp,
            image1,
            image2,
            nx,
            ny,
            deltat,
            deltas,
            sigma,
            vx,
            vy,
            vm,
            thresh,
            absflag,
            filter,
            kr,
            skip,
            poff,
            qoff,
            interp,
            latmin,
            latmax,
            biascor,
            verbose,
        )
    else:
        ierflct, vx_c, vy_c, vm_c = _pyflct.pyflct(
            transp,
            image1,
            image2,
            nx,
            ny,
            deltat,
            deltas,
            sigma,
            vx,
            vy,
            vm,
            thresh,
            absflag,
            filter,
            kr,
            skip,
            poff,
            qoff,
            interp,
            biascor,
            verbose,
        )

    # The arrays returned from the FLCT C function are actually 2D arrays but stored as
    # single dimension array. So after getting them we need to reshape them in the original
    # shape of the input images.
    vx_c = vx_c.reshape((nx, ny))
    vy_c = vy_c.reshape((nx, ny))
    vm_c = vm_c.reshape((nx, ny))

    return (vx_c, vy_c, vm_c)
