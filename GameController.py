import enum
import time

ID, XPOS, YPOS = 0, 1, 2
POS, NEG = 0, 1

class HandLandmark(enum.IntEnum):
  """The 21 hand landmarks."""
  WRIST = 0
  THUMB_CMC = 1
  THUMB_MCP = 2
  THUMB_IP = 3
  THUMB_TIP = 4
  INDEX_FINGER_MCP = 5
  INDEX_FINGER_PIP = 6
  INDEX_FINGER_DIP = 7
  INDEX_FINGER_TIP = 8
  MIDDLE_FINGER_MCP = 9
  MIDDLE_FINGER_PIP = 10
  MIDDLE_FINGER_DIP = 11
  MIDDLE_FINGER_TIP = 12
  RING_FINGER_MCP = 13
  RING_FINGER_PIP = 14
  RING_FINGER_DIP = 15
  RING_FINGER_TIP = 16
  PINKY_MCP = 17
  PINKY_PIP = 18
  PINKY_DIP = 19
  PINKY_TIP = 20

class GameControl():

    def __init__( self ) :
        self.distanceState = POS # record positvie or negative
        self.step = 0
        self.preTimeRecordStep = 0
        self.velocity = 0
        self.curTime = 0
        self.preTime = 0
        self.perSecondStaringTime = time.time()

    def Run( self, img, *handLandMarkPosition ):
        self.handLandMarkPosition = handLandMarkPosition
        #print( self.handLandMarkPosition[5] )
        #print(self.IsReady())
        if len(self.handLandMarkPosition) != 0 :
            if ( self.IsReady() ):
                
                self.IsOneStep( distanceTurnOut = 20 )
                #print( "step:", self.step )
                
                #print(passASecond)
                if ( self.IsOneSecond() ):

                    self.CalculatingVelocity(0.7, 0.3)
                    print( "velocity( steps/ per second): ", self.velocity )

        elif ( self.IsOneSecond() ):
            self.CalculatingVelocity( 0.15, 0.85 )
            print( "velocity( steps/ per second): ", self.velocity )


    def CalculatingVelocity( self, a = 0.8, b = 0.2 ):
        Bias = ( self.step - self.preTimeRecordStep )
        print( Bias )
        self.velocity = round((self.velocity*a + Bias*b), 1) # normalize the velocity
        self.preTimeRecordStep = self.step


    def IsOneSecond( self ) :

        if ( (self.curTime - self.perSecondStaringTime) >= 1 ):
            self.perSecondStaringTime = self.curTime
            return True
        else:
            return False
        

    def InitPerSecondStartingTime(self):
        self.perSecondStaringTime = self.curTime


    def GetFPS( self ):
        self.curTime = time.time()
        fps = 1 / (self.curTime - self.preTime )
        self.preTime = self.curTime

        return fps


    def GetStep( self ):
        return self.step


    def GetVelocity( self ):
        return self.velocity


    def IsReady( self ) :
        #print( self.handLandMarkPosition[5] )
        if ( self.handLandMarkPosition[HandLandmark.INDEX_FINGER_TIP][YPOS] > self.handLandMarkPosition[HandLandmark.INDEX_FINGER_MCP][YPOS] and
             self.handLandMarkPosition[HandLandmark.MIDDLE_FINGER_TIP][YPOS] > self.handLandMarkPosition[HandLandmark.MIDDLE_FINGER_MCP][YPOS] ):
            return True
        else:
            return False


    def IsOneStep( self, distanceTurnOut = 50 ):
        indexFingerTip_Xpos = self.handLandMarkPosition[HandLandmark.INDEX_FINGER_TIP][XPOS]
        middleFingerTip_Xpos = self.handLandMarkPosition[HandLandmark.MIDDLE_FINGER_TIP][XPOS]
        
        distance = self.CalculateDistance( indexFingerTip_Xpos, middleFingerTip_Xpos )

        if ( distance >= 0 and self.distanceState == NEG ):
            if ( abs( distance ) > distanceTurnOut ):
                self.step += 1
                self.distanceState = POS

        elif ( distance < 0 and self.distanceState == POS ):
            if ( abs( distance ) > distanceTurnOut ):
                self.step += 1
                self.distanceState = NEG


    def CalculateDistance( self, X1, X2 ):
        return (X1 - X2)
        #self.handLandMarkPosition[HandLandmark.INDEX_FINGER_TIP]
    