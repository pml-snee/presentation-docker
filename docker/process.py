import netCDF4 as nc
import sys

def run( inputFile, outputFile):

    ncfile     = nc.Dataset( inputFile)
    outputList = []

    print( "Processing {}".format( outputFile))
    
    for v in ncfile.variables:
        outputList += [str(v)]

    print( outputList)
    outputFile = open( outputFile, "w+")
    outputFile.write( "\n".join( outputList))

    print( "Processing complete")


if '__main__' == __name__:

    args = sys.argv[1:]

    if len( args) < 2:
        print( "Error: missing file names")
    else:
        run( args[0], args[1])
